import math

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count(): return -1
        elif page_index < self.page_count() - 1: return self.items_per_page
        else: return (self.item_count()-1) % self.items_per_page + 1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count(): return -1 
        else: return math.floor(item_index / self.items_per_page)

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print('Collection = ' + str(helper.collection))
print('Items per page = ' + str(helper.items_per_page))
print('Page count = ' + str(helper.page_count()) + ' -- Should == 2')
print('Item count = ' + str(helper.item_count()) + ' -- Should == 6')
print('Page item count (0) = ' + str(helper.page_item_count(0)) + ' -- Should == 4')
print('Page item count (1) = ' + str(helper.page_item_count(1)) + ' -- Last page - should == 2')
print('Page item count (2) = ' + str(helper.page_item_count(2)) + ' -- Should == -1 since the page is invalid')

# page_index takes an item index and returns the page that it belongs on
print('Page index (0) = ' + str(helper.page_index(0)) + ' -- Should == 0 (zero based index)')
print('Page index (5) = ' + str(helper.page_index(5)) + ' -- Should == 1 (zero based index)')
print('Page index (2) = ' + str(helper.page_index(2)) + ' -- Should == 0')
print('Page index (20) = ' + str(helper.page_index(20)) + ' -- Should == -1')
print('Page index (-10) = ' + str(helper.page_index(-10)) + ' -- Should == -1 because negative indexes are invalid')

# Edge case: List [1,2,3,4] with 4 items per page
edge = PaginationHelper([1, 2, 3, 4], 4)
print('Page count = ' + str(edge.page_count()) + ' -- Should be 1')
print('Page item count (0) = ' + str(edge.page_item_count(0)) + ' -- Should == 4')