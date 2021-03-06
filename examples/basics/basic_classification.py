__author__ = "Max Dippel, Michael Burkart and Matthias Urban"
__version__ = "0.0.1"
__license__ = "BSD"

import os, sys
sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
from autoPyTorch import AutoNetClassification
from autoPyTorch.data_management.data_manager import DataManager

# Note: You can write your own datamanager! Call fit with respective train, valid data (numpy matrices) 
dm = DataManager()
dm.generate_classification(num_classes=3, num_features=21, num_samples=1500)

# Note: every parameter has a default value, you do not have to specify anything. The given parameter allow a fast test.
autonet = AutoNetClassification(budget_type='epochs', min_budget=1, max_budget=9, num_iterations=1, log_level='info')

res = autonet.fit(X_train=dm.X, Y_train=dm.Y, X_valid=dm.X_train, Y_valid=dm.Y_train)

print(res)
print("Score:", autonet.score(X_test=dm.X_train, Y_test=dm.Y_train))
