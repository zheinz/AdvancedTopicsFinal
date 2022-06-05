# AdvancedTopicsFinal
Copy of my final system for Advanced Topics in Computer Science

Running trainModel.py will train a model identically to the models used in the paper. However, the models may differ depending on the versions of python and other libraries being used. 

Running renderGame.py will play a game with the trained model by specifying the correct path to one of the models checkpoints. In this script the permutation and/or noisy attacks can be applied.

Results.py contains the script to recreate the graphs used in the final paper however the directories in the script will need updating according to the individuals machine and where the results are saved.

The results directory contains three subdirectories; baselines, noise, permutation. Baslines contains the baselines for all three models. Noise and permutation contains the results of the noise and permutation attacks following the naming format (model, attack, noise amount/permutation probability). Therefore, M1N05 is model 1 noise amount 5% and M2P90 is model 2 permutation 90% etc. Within each file is the results of 100 games for each configuration where line 1 is the reward for game 1, line 2 is the number of cycles for game 1, line 3 is reward for game 2, line 4 is the number of cycles for game 2 and so forth. Therefore, the results alternate between reward and number of cycles per game for 100 games, this is how averages were calculated in the report. 
