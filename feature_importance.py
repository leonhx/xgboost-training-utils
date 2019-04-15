#!/usr/bin/env python

import xgboost as xgb
import sys

def get_feature_importance(model_file, fmap=None):
    if fmap is not None:
        with open(fmap) as f:
            _features = [line.split() for line in f.readlines()]
            feature_map = {('f%s' % f[0]):f[1] for f in _features}
    else:
        feature_map = {}
    bst = xgb.Booster(model_file=model_file)
    weights = bst.get_score(importance_type='weight')
    gains = bst.get_score(importance_type='gain')
    covers = bst.get_score(importance_type='cover')
    all_fids = set(weights.keys()) | set(gains.keys()) | set(covers.keys())
    summary = {}
    for fid in all_fids:
        fname = feature_map.get(fid, fid)
        weight = weights.get(fid, 0)
        gain = gains.get(fid, 0.0)
        cover = covers.get(fid, 0.0)
        summary[int(fid[1:])] = (fname, weight, gain, cover)
    return summary

def main():
	model_file = sys.argv[1]
	fmap = None
	if len(sys.argv) > 2:
	    fmap = sys.argv[2]
	print('\t'.join(['feature_id', 'feature_name', 'weight', 'gain', 'cover']))
	for fid, (fname, weight, gain, cover) in get_feature_importance(model_file, fmap).items():
		print('\t'.join([str(fid), fname, str(weight), str(gain), str(cover)]))

if __name__ == '__main__':
    main()
