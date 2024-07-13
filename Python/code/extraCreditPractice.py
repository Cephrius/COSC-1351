
## Warmup 1

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

#print(sleep_in(False,True))

## Warmup 2
def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

## print(monkey_trouble(False,False))

## Warmup 3

def sum_double(a,b):
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum

print(sum_double(1,2))

## Warmup 4

def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2

#print(diff21(40))
## print(diff21())


## Warmup 5
def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))

#print(parrot_trouble(True,19))

## Warmup 6
def makes10(a , b):
    return (a == 10 or  b == 10 or a + b == 10)

#print(makes10(10,9))

## Warmup 7
def near_hundred(n):
    return ((abs(100 - n ) <= 10 or abs(200 - n) <= 10))
#print(near_hundred(99))

## Warmup 8
def pos_neg(a , b ,negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))
#print(pos_neg(-4,-5,True))

## Warmup 9
def not_string(str):
   if str.startswith("not"):
       return str
   else:
       return"not {}".format(str)

## Warmup 10
def missing_char(str, n):
    number = str[n]
    new = str.replace(number,"")
    return new


## Warmup 11
def front_back(str):
    if len(str) <= 1:
        return str
    middle = str[1:len(str)-1]
    return str[len(str)-1] + middle + str[0]

#print(front_back('o'))

## Warmup 12
def front3(str):
     first_three = str[0:3]
     if len(str) < 3:
         str = first_three
     return first_three + first_three + first_three
#print(front3('ab'))
################################################################

# WARMUP SECTION 2

# Warmup 1
def string_times(str, n):
    string = ""
    for i in range(n):
        string += str
    return string

# Warmup 2
def front_times(str,n):
    front_len = 3
    front = str[:front_len]
    result = ""

    for i in range(n):
        result = result + front
    return result

#print(front_times('Chicken',5))

# Warmup 3
def string_bits(str):
    result = ""
    for i in range(0,len(str),2):
        result = result + str[i]
    return result
#print(string_bits('Hello'))

# Warmup 4
def string_splosion(str):
    result = ""
    for num in range (len(str)):
        result += str[0:num]
    return result + str
#print(string_splosion("ab"))

# Warmup 5
def last2(str):
    if len(str) < 2:
        return 0
    last2 = str[-2:]
    count = 0
    for i in range(len(str)-2):
        sub_string = str[i:i+2]
        if sub_string == last2:
            count += 1
    return count

#print(last2("axxxaaxx"))

# Warmup 6
def array_count9(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count

#print(array_count9([2,3,7,8,8,7]))

# Warmup 7
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False
#print(array_front9([1,2,7,7,9]))

# Warmup 8
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

#print(array123([1,1,1,2,3,1,1,2]))

# Warmup 9
def string_match(a,b):
    shorter = min(len(a),len(b))
    count = 0

    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count += 1
    return count
#print(string_match('adbced','abc'))

# Warmup Section 3

# Warmup 1
def hello_name(name):
    return "Hello " + name + "!"
print(hello_name("Alan"))

# Warmup 2
def make_abba(a,b):
    return a + b + b + a

# Warmup 3
def make_tags(tag,word):
    return "<{}>{}</{}>".format(tag,word,tag)

print(make_tags("i","Chicken"))

# Warmup 4
def make_out_word(out,word):
    return out[0:2] + word + out[2:4]

print(make_out_word("<<>>","Yay"))

# Warmup 5
def extra_end(str):
    end = str[-2:]
    return end + end + end

# Warmup 6
def first_two(str):
    two = str[2:]
    return two

# Warmup 6
def first_half(str):
    if len(str) % 2 == 0:
        return str[0:len(str)//2]


print(first_half("HelloWorld"))

# Warmup 7
def without_end(str):
    return str[1:-1]

print(without_end("java"))

# Warmup 8
def combo_string(a,b):
    return min(a,b, key=len) + max(a,b, key=len) + min(a,b, key=len)

print(combo_string("Hello","hi"))

# Warmup 9
def non_start(a, b):
    return a[1:] + b[1:]

print(non_start("Hello","Java"))

# Warmup 10
def left2(str):
    left2 = str[0:2]
    return str[2:] + left2

print(left2("Hello"))


# Warmup Section 4

# Warmup 1
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        return True
    else:
        return False

print(first_last6([1,2,6,6]))

# Warmup 2
def same_first_last(nums):
    if nums[len(nums)] > 0 and nums[0] == nums[-1]:
        return True
    else:
        return False

# Warmup 3
def make_pi():
    return [3,1,4]

print(make_pi())

# Warmup 4
def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False

# Warmup 5
def sum3(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print(sum3([1,2,5]))

# Warmup 6
def rotate_left3(nums):
    nums[0],nums[1],nums[2] = nums[1],nums[2],nums[0]
    return nums

# Warmup 7
def reverse3(nums):
    nums.reverse()
    return nums

# Warmup 8
def max_end3(nums):
    list = []
    setnum = max(nums[0],nums[-1])
    for i in range(3):
        list.append(setnum)
    return list

# Warmup 9
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) < 2:
    sum = 0
    for num in nums:
      sum += num
    return sum
  else:
    return 0

# Warmup 10
def middle_way(a, b):
    middle = []
    middle.append(a[1])
    middle.append(b[1])
    return middle

# Warmup 11
def make_ends(nums):
    front_and_end = [nums[0],nums[-1]]
    return front_and_end

# Warmup 12
def has23(nums):
    if 3 in nums or 2 in nums:
        return True
    else:
        return False

print(has23([2,3]))

# Warmup Section 5

# Warmup 1
def cigar_party(cigar, is_weekend):
    if is_weekend:
        return 40 <= cigar
    if not is_weekend:
        return 40 <= cigar <= 60


print(cigar_party(55,False))

# Warmup 2
def date_fashion(you, date):
    if you <= 2 or date <= 2:
      return 0
    elif you >= 8 or date >= 8:
      return 2
    else:
      return 1

# Warmup 3
def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    if not is_summer:
        return 60 <= temp <= 90

# Warmup 4
def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed < 61:
      return 0
    elif speed > 60 and speed < 81:
      return 1
    elif speed > 80:
      return 2
  if is_birthday:
    if speed < 66:
      return 0
    elif speed > 60 and speed < 86:
      return 1
    else:
      return 2

# Warmup 5
def sorta_sum(a, b):
    sum = a + b
    if sum >= 10 and sum <= 19:
        return 20
    else:
        return sum

# Warmup 6
def alarm_clock(day, vacation):
  if vacation:
    if day in (0, 6):
      return "off"
    else:
      return "10:00"
  else:
    if day in (0, 6):
      return "10:00"
    else:
      return "7:00"

# Warmup 7
def love6(a, b):
  return a == 6 or b == 6 or a + b == 6 or (a - b) == 6


# Warmup 8
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    if not outside_mode:
        return 1 <= n <= 10

# Warmup 9
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

# Warmup Setion 6

# Warmup 1
