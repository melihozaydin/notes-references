"""
Iterable: something that can be looped over. object needs to return an iterable from its __iter__ object
and the iterator that is returned must define a __next__ which accesses values from the container one at a time

just because something is an iterator doesnt mean they are iterable

Iterable objects have built in dunder method __iter__ in them which can be found with dir(object)
__iter method of thew object is an iterator.

Iterators have __next__ method built in which can be found the same way as before

next(Iterator) returns the next value of the iterator. it will remember its index for which value to return next.
if we run out of values it will raise an stopiteration exception.

when we run a for loop on a list :
while true:
    try:
        item = next(Iterable)
        print(item)
    except StopIteration:
        break

"""

##Practical example
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end
    ##now to make this class iterable
    
    def __iter__(self):
        return self
    #to make an iterator for thew iterable myrange object we make it retur self then add a __next__ to its 'self' 
    # so myrange has its __iter__ object to be an iterable 
    # and self.__iter__ has a __next__ method to be an iterator.  
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)
print(next(nums))
print(next(nums))
print(next(nums))
# until we hit StopIteration exception

print('---iterators with generators---')
# generators are iterators as well but __iter__ and __next__ are built in autamatically
#they also remember the last yield just like iterator.
def my_range(start, end):
    # iterators can go on forever as long as there is a next value
    # so we could remove end parameter here and put in while true below and it would count forever
    current = start
    while current < end:
        yield current
        current += 1

##Nums is an iterabla
nums = my_range(1, 10)

for num in nums:
    print(num)

"""
Iterators are usefeul for writing memory efficient programs. (just like generators)

"""