# https://maciejkula.github.io/spotlight/

# /Users/matthiaszimmermann/Documents/private/18_incubator_sept
# docker-compose build
# docker run --rm -it --init --volume=$PWD:/app matthiaszimmermann/spotlight python3 amazon.py

from spotlight.cross_validation import random_train_test_split
from spotlight.datasets.amazon import get_amazon_dataset
from spotlight.evaluation import rmse_score
from spotlight.evaluation import mrr_score
from spotlight.factorization.explicit import ExplicitFactorizationModel
from spotlight.factorization.implicit import ImplicitFactorizationModel

dataset = get_amazon_dataset(min_user_interactions=20, min_item_interactions=50)

train, test = random_train_test_split(dataset)

model_explicit = ExplicitFactorizationModel(n_iter=1)
# model_implicit = ImplicitFactorizationModel(n_iter=3, loss='bpr')

model_explicit.fit(train)
# model_implicit.fit(train)

print("test user_ids")
print(test.user_ids)

print("test item_ids")
print(test.item_ids)

print("test timestamps")
print(test.timestamps)

print("test weights")
print(test.weights)

score_explicit = rmse_score(model_explicit, test)
# score_implicit = mrr_score(model_implicit, test)

print("rmse score for explicit model: %.3f" % score_explicit)
# print("mrr score for implicit model")
# print(score_implicit)
