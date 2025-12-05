from mat73 import loadmat
import numpy as np

# Load the subset file -- ensure 'data/Train_Subset.mat' exists!
data = loadmat('data/Train_Subset.mat')

signals = data['Subset']['Signals']  # (segments, channels, samples)

# By convention, ABP is channel 2 (0=ECG, 1=PPG, 2=ABP)
ABP_channel = 2
abp_segments = signals[:1000, ABP_channel, :]  # Grab first 1000 segments, ABP only

# Save result as a NumPy binary
np.save('data/abp_1000_segments.npy', abp_segments)

print(f'Extracted shape: {abp_segments.shape}')
print('Extraction complete. Data saved as data/abp_1000_segments.npy')