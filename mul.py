# -*- coding:utf-8 -*-
# @Time    : 10/30/23 5:38 PM
# @Author  : wlj

import argparse
import random

def make_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--path',
                        help='txt path that save directory of datasets',
                        type=str,
                        default='',
                        required=True)
    return parser

# 基础乘法口诀表
def multiply_base(num_range=10):
    [a, b] = random.sample(range(1, num_range), 2)
    r = a * b
    ans = "%-3d * %-3d = %-3d" % (a, b, r)
    q = "%-3d * %-3d = " % (a, b)
    return ans, q

# 统一函数的格式
def fun_mul(rows, cols, num_range, row_format="\n", col_format="            "):
    answer = ""
    ques = ""
    for i in range(rows):
        for j in range(cols):
            ans, q = multiply_base(num_range)
            if j == cols - 1:
                format = row_format
            else:
                format = col_format
            answer += ans + format
            ques += q + format
    return answer, ques


if __name__ == '__main__':
    args = make_parser().parse_args()
