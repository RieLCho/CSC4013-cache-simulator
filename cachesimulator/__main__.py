#!/usr/bin/env python3

import argparse

from simulator import Simulator


# Parse command-line arguments passed to the program
def parse_cli_args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--cache-size", type=int, required=True, help="the size of the cache in words"
    )

    parser.add_argument(
        "--num-blocks-per-set", type=int, default=1, help="the number of blocks per set"
    )

    parser.add_argument(
        "--num-words-per-block",
        type=int,
        default=1,
        help="the number of words per block",
    )

    parser.add_argument(
        "--word-addrs",
        nargs="+",
        type=int,
        required=True,
        help="one or more base-10 word addresses",
    )

    parser.add_argument(
        "--num-addr-bits",
        type=int,
        default=1,
        help="the number of bits in each given word address",
    )

    parser.add_argument(
        "--replacement-policy",
        choices=("lru", "mru"),
        default="lru",
        # Ignore argument case (e.g. "mru" and "MRU" are equivalent)
        type=str.lower,
        help="the cache replacement policy (LRU or MRU)",
    )

    return parser.parse_args()


def main():
    # 지역성을 보여주는 예제 워크로드
    example_workload = [
        1, 2, 3, 4,  # 순차적 접근
        1, 2, 3, 4,  # 같은 데이터 재접근
        10, 11, 12,  # 다른 영역 접근
        1, 2, 3, 4   # 다시 처음 데이터로 돌아옴
    ]
    
    sim = Simulator()
    sim.run_simulation(
        cache_size=8,
        num_blocks_per_set=2,
        num_words_per_block=2,
        replacement_policy="lru",
        num_addr_bits=8,
        word_addrs=example_workload
    )

if __name__ == "__main__":
    main()
