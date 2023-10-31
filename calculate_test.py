# -*- coding:utf-8 -*-
# @Time    : 10/30/23 6:53 PM
# @Author  : wlj

import argparse
import random
import numpy as np
from log import logger
from application import problem
from plus import *
from mul import *
def make_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--path',
                        help='txt path that save directory of datasets',
                        type=str,
                        default='')
    return parser


if __name__ == '__main__':
    args = make_parser().parse_args()
    rows = 7
    cols = 3
    num_range = 100

    logger.info("日期：______________    完成时间：______________    得分：______________\n")
    logger.info("一、口算题")

    # 统一函数的格式
    # answer, ques = fun_plus(rows, cols, num_range, func=plus_3_number, row_format="\n")
    answer, ques = fun_plus_custom(5, cols, num_range, row_format="\n")
    logger.info("%s" % ques)
    logger.debug("%s" % answer)

    logger.info("二、乘法")
    answer, ques = fun_mul(3, cols, 10, row_format="\n")
    logger.info("%s" % ques)
    logger.debug("%s" % answer)

    logger.info("三、笔算题")
    answer, ques = fun_plus(3, cols, num_range, func=plus_3_number, row_format="\n\n\n\n\n\n", col_format="          ")
    logger.info("%s" % ques)

    logger.info("四、应用题")

    counts = len(problem)
    idx = random.randint(0, counts - 1)
    str = problem[idx]
    logger.info(str)
