def two_sum1(nums, target):
    found_so_far = {}

    for i in range(len(nums)):
        found_so_far[nums[i]] = i

    for n in nums:
        if target - n in found_so_far:
            return [found_so_far[target - n], found_so_far[n]]

def two_sum(nums, target):
    found_so_far = {}

    for i in range(len(nums)):
        need_to_find = target - nums[i]

        if need_to_find in found_so_far:
            return [i, found_so_far[need_to_find]]
        
        found_so_far[nums[i]] = i



def main():
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum1(nums, target))

if __name__ == "__main__":
    main()