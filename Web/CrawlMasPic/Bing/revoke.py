# -*- coding: utf-8 -*-
from config import *
from tqdm import tqdm

cp_lines = [line.split('\t')[-1]+'.jpg' for line in LoadTxtToLines(cp_path) if 'Failed' not in line]

