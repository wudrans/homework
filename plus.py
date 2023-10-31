# -*- coding:utf-8 -*-
# @Time    : 10/19/23 8:54 AM
# @Author  : wlj

import argparse
import random
import numpy as np
from log import logger
from application import problem

def make_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--rows',
                        help='rows', type=int,default=6)
    parser.add_argument('--cols',
                        help='cols', type=int,default=3)

    parser.add_argument('--rows2',
                        type=int,default=3)
    parser.add_argument('--cols2',
                        type=int,default=3)
    parser.add_argument('--num_range',
                        type=int, default=20)

    return parser


# 数值本身和结果都控制在一个范围内，该范围由外部确定，与a,b相同范围
def operation_2(a, b):
    op = random.choice(["+", "-"])
    if op == "-":
        v1 = a if a >= b else b
        v2 = a if a < b else b
        v3 = v1 - v2
    else:
        v3 = a if a >= b else b
        v2 = a if a < b else b
        v1 = v3 - v2
    # s = "%d %s %d = %3d" % (v1, op, v2, v3)
    return [v1, v2, v3], op

# 2个数加减
def plus_2_number(num_range):
    [a, b] = random.sample(range(0, num_range + 1), 2)
    number, op = operation_2(a, b)
    ans = "%-3d %s %-3d = %-3d" % (number[0], op, number[1], number[2])
    q = "%-3d %s %-3d = " % (number[0], op, number[1])
    return ans, q

def plus_3_number(num_range):
    [a, b] = random.sample(range(0, num_range + 1), 2)
    number, op = operation_2(a, b)

    c = random.randint(0, num_range)  # [0, 100]
    number2, op2 = operation_2(number[2], c)

    if number2[0] == number[2]:
        ans = "%-3d %s %-3d %s %-3d = %-3d" % (number[0], op, number[1], op2, number2[1], number2[2])
        q = "%-3d %s %-3d %s %-3d = " % (number[0], op, number[1], op2, number2[1])
    elif number2[1] == number[2]:
        if op2 == "-":
            if op == "+":
                op = "-"
            else:
                op = "+"
        ans = "%-3d %s %-3d %s %-3d = %-3d" % (number2[0], op2, number[0], op, number[1], number2[2])
        q = "%-3d %s %-3d %s %-3d = " % (number2[0], op2, number[0], op, number[1])
    elif number2[2] == number[2]:
        if op == "+":
            op = "-"
        else:
            op = "+"
        ans = "%-3d %s %-3d %s %-3d = %-3d" % (number2[0], op2, number2[1], op, number[1], number[0])
        q = ("%-3d %s %-3d %s %-3d = ") % (number2[0], op2, number2[1], op, number[1])

    return ans, q

# 统一函数的格式
def fun_plus(rows, cols, num_range, func, row_format="\n", col_format="            "):
    answer = ""
    ques = ""
    for i in range(rows):
        for j in range(cols):
            ans, q = func(num_range)
            if j == cols - 1:
                format = row_format
            else:
                format = col_format
            answer += ans + format
            ques += q + format
    return answer, ques


def fun_plus_custom(rows, cols, num_range, row_format="\n", col_format="            "):
    answer = ""
    ques = ""
    for i in range(rows):
        for j in range(cols):
            if j == 0:
                ans, q = plus_2_number(num_range)
            else:
                ans, q = plus_3_number(num_range)
            if j == cols - 1:
                format = row_format
            else:
                format = col_format
            answer += ans + format
            ques += q + format
    return answer, ques


if __name__ == '__main__':
    args = make_parser().parse_args()
    rows = args.rows
    cols = args.cols
    rows2 = args.rows2
    cols2 = args.cols2
    num_range = args.num_range


    logger.info("日期：______________    完成时间：______________    得分：______________\n")
    logger.info("一、口算题")

    # 统一函数的格式
    # answer, ques = fun_plus(rows, cols, num_range, func=plus_3_number, row_format="\n")
    answer, ques = fun_plus_custom(rows, cols, num_range, row_format="\n")
    logger.info("%s" % ques)
    logger.debug("%s" % answer)

    logger.info("二、笔算题")
    answer, ques = fun_plus(rows, cols, num_range, func=plus_3_number, row_format="\n\n\n\n\n")
    logger.info("%s" % ques)

    logger.info("三、应用题")

    counts = len(problem)
    idx = random.randint(0, counts - 1)
    str = problem[idx]
    logger.info(str)




