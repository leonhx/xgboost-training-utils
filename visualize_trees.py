#!/usr/bin/env python

import xgboost as xgb
import sys

def main():
	out_dir = sys.argv[1]
	model_file = sys.argv[2]
	bst = xgb.Booster(model_file=model_file)
	num_trees = len(bst.get_dump())
	if len(sys.argv) > 3:
	    with open(sys.argv[3]) as f:
			features = [line.split() for line in f.readlines()]
			bst.feature_names = [f[1] for f in features]
			bst.feature_types = [f[2] for f in features]
	for i in range(num_trees):
		sys.stdout.write('\rtree id: %d' % i)
		graph = xgb.to_graphviz(bst, i)
		graph.format = 'png'
		graph.render(str(i), directory=out_dir, view=False, cleanup=True)

if __name__ == '__main__':
    main()
