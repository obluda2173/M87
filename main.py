import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np

CSV_PATH = "./csv/*.csv"
N = 512  # Grid size for imaging

def load_data(csv_path):
	"""Reads all CSV files in the given path and combines them into a single DataFrame."""
	column_names = ["time(UTC)", "T1", "T2", "U(lambda)", "V(lambda)", "Iamp(Jy)", "Iphase(d)", "Isigma(Jy)"]
	df_list = [pd.read_csv(file, comment="#", names=column_names, skiprows=1) for file in glob.glob(csv_path)]
	return pd.concat(df_list, ignore_index=True)

def plot_uv_coverage(df):
	"""Plots the UV coverage from the combined dataset."""
	plt.figure(figsize=(8, 6))
	plt.scatter(df["U(lambda)"], df["V(lambda)"], s=5, alpha=0.5, label="UV Points")
	plt.xlabel("U (lambda)")
	plt.ylabel("V (lambda)")
	plt.title("UV Coverage from All Files")
	plt.legend()
	plt.grid(True)
	plt.show(block=False)

def reconstruct_image(df):
	"""Performs inverse Fourier Transform for naive image reconstruction."""
	u_vals, v_vals = df["U(lambda)"].values, df["V(lambda)"].values
	amps, phases = df["Iamp(Jy)"].values, df["Iphase(d)"].values

	# Normalize U and V to fit in grid indices
	u_min, u_max = u_vals.min(), u_vals.max()
	v_min, v_max = v_vals.min(), v_vals.max()

	u_idx = ((u_vals - u_min) / (u_max - u_min) * (N - 1)).astype(int)
	v_idx = ((v_vals - v_min) / (v_max - v_min) * (N - 1)).astype(int)

	# Initialize UV grid
	uv_grid = np.zeros((N, N), dtype=complex)

	# Populate grid
	for i in range(len(u_vals)):
		uv_grid[u_idx[i], v_idx[i]] = amps[i] * np.exp(1j * np.radians(phases[i]))

	# Inverse FFT with shift correction
	image = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(uv_grid))).real

	# Plot reconstructed image
	plt.figure(figsize=(6, 6))
	plt.imshow(image, cmap="inferno", extent=[u_min, u_max, v_min, v_max])
	plt.colorbar(label="Intensity")
	plt.title("Naïve Image Reconstruction")
	plt.xlabel("U (lambda)")
	plt.ylabel("V (lambda)")
	plt.show(block=False)

def main():
	"""Main function to execute data loading, plotting, and image reconstruction."""
	df = load_data(CSV_PATH)

	plot_uv_coverage(df)
	reconstruct_image(df)

	plt.pause(0.1)
	input("Press Enter to close plots...")

if __name__ == "__main__":
	main()