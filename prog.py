import argparse
def mean(nums:list):
  return sum(nums)/len(nums)
def median(nums:list):
  nums = sorted(nums)
  n = len(nums)
  if n % 2 == 0:
    middle_num1 = nums[n//2]
    middle_num2 = nums[n//2 -1]
    median_num = (middle_num1 + middle_num2)/2
    return median_num
  else:
    median_num = nums[n//2]
    return median_num
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('-m', dest='accumulate', action='store_const',
                    const=median, default=mean,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))
