
if __name__ == "__main__":
    with open("problem067.txt") as f:
        lines = [line for line in f.readlines()]
    prev_nums, cur_nums = None, None
    for line in lines[-1::-1]:
        prev_nums, cur_nums = cur_nums, [int(s) for s in line.split(" ")]
        if prev_nums:
            for i in range(len(cur_nums)):
                cur_nums[i] += max(prev_nums[i], prev_nums[i+1])
    print cur_nums[0]

