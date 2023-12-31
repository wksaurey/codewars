# my solution. Same time complexity o(n) but much worse memory complexity o(n)
def loop_size(node):
    visited = set()
    while node not in visited:
        visited.add(node)
        node = node.next
    current = node.next
    length = 1
    while current != node:
        current = current.next
        length += 1
    return length

# best practice time o(n) space o(1)
def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    # Find a point in the loop.  Any point will do!
    # Since the rabbit moves faster than the turtle
    # and the kata guarantees a loop, the rabbit will
    # eventually catch up with the turtle.
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    # The turtle and rabbit are now on the same node,
    # but we know that node is in a loop.  So now we
    # keep the turtle motionless and move the rabbit
    # until it finds the turtle again, counting the
    # nodes the rabbit visits in the mean time.
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    # voila
    return count