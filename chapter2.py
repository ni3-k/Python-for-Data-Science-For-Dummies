from sklearn.datasets import load_boston

boston = load_boston()

items = dir(boston)

for item in items:
	if 'key' in item:
		print(item)

print(boston.keys())

print(boston.feature_names)