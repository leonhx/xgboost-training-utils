#!/usr/bin/env python

import xgboost as xgb
import sys

if __name__ == '__main__':
    xgb.Booster(model_file=sys.argv[1]).dump_model(sys.stdout)
