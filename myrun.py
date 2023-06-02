"""
My Script
=========

Script to present the use of XParams,
through a Makefile.

RUN: python myrun.py
"""
from datetime import date
from xparams import XParams


def main():
    defaults = {
        "param": "myparam",
        "section": {
            "subsection1": {
                "param1": 500,
                "param2": True,
                "param3": "foo",
                "param4": [1, 2, 3],
            },
            "subsection2": {
                "param1": False,
                "param2": 2.0,
                "param3": date(2023, 6, 3),
                "param4": -1,
                "param5": {
                    "var1": 1,
                    "var2": "2",
                },
            },
        },
    }

    params = XParams(defaults, user_params_dir='config', verbose=False)
    params5 = params.section.subsection2.param5
    for _ in range(params5.var1):
        print(
            ">>>> I'll print this as many time as"
            f" params.section.subsection2.param5: {params5.var1}"
        )


if __name__ == '__main__':
    main()
