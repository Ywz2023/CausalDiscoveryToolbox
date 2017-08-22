"""
Settings file for CGNN algorithm
Defining all global variables
Authors : Anonymous Author
Date : 8/05/2017
"""


class DefaultSettings(object):
    __slots__ = ("h_layer_dim",
                 "train_epochs",
                 "test_epochs",
                 "NB_RUNS",
                 "NB_JOBS",
                 "GPU",
                 "NB_GPU",
                 "GPU_OFFSET",
                 "learning_rate",
                 "init_weights",
                 "nb_run_feature_selection",
                 "regul_param",
                 "threshold_UMG",
                 "nb_epoch_train_feature_selection",
                 "nb_epoch_eval_weights",
                 "use_Fast_MMD",
                 "nb_vectors_approx_MMD",
                 "complexity_graph_param",
                 "model_confounder",
		 "max_nb_points")

    def __init__(self):  # Define here the default values of the parameters
        self.NB_RUNS = 32
        self.NB_JOBS = 2
        self.GPU = True
        self.NB_GPU = 2
        self.GPU_OFFSET = 0
        self.learning_rate = 0.01
        self.init_weights = 0.05
        self.max_nb_points = 1500

        # CGNN
        self.h_layer_dim = 20
        self.train_epochs = 1000
        self.test_epochs = 500
        self.use_Fast_MMD = False
        self.nb_vectors_approx_MMD = 100
        self.complexity_graph_param = 0.0007
        self.model_confounder = 1

        # specific for FSGNN
        self.nb_run_feature_selection = 1
        self.regul_param = 0.004
        self.threshold_UMG = 0.15
        self.nb_epoch_train_feature_selection = 2000
        self.nb_epoch_eval_weights = 500


SETTINGS = DefaultSettings()
