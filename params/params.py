#K, path_to_chkpt, path_to_backup, path_to_Wi, batch_size, path_to_preprocess, frame_shape, path_to_mp4

#number of frames to load
K = 1 #8

#path to main weight
path_to_chkpt = 'model_weights.tar' 

#path to backup
path_to_backup = 'backup_model_weights.tar'

#CHANGE first part
path_to_Wi = ""+"Wi_weights"
#path_to_Wi = "test/"+"Wi_weights"

#CHANGE if better gpu
batch_size = 2

#dataset save path
path_to_preprocess = '/content/face-alignment/test/assets/VoxCeleb/'#/mnt/ACA21355A21322FE/VoxCeleb/saves2'

#default for Voxceleb
frame_shape = 224

#path to dataset
path_to_mp4 = '/content/face-alignment/test/assets/VoxCeleb/mp4' #/mnt/ACA21355A21322FE/VoxCeleb/vox2_mp4/dev/mp4'
