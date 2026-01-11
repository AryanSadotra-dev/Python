

I.>
# what is list 
-> A list is a data structure used to store multiple values inside a single variable in a specific order.

-> Key definition points:

*.One variable → many values-> A single variable name can store multiple values together.
  ex : nums = [10, 20, 30]

*.Values are stored sequentially-> Elements are stored one after another in a fixed order.
  Example: nums = [10, 20, 30, 40]

*. Each value has a position (index)-> Every element has a numbered position, starting from 0.
 ex: nums = [10, 20, 30, 40]
 Index	Value
 0	    10
 1	    20
 2	    30
 3	    40

*.Data can be changed after creation : You can modify, add, or remove elements after the list is created.
 ex: nums = [10, 20, 30]
 nums[1] = 99      # change
 nums.append(40)  # add
 nums.remove(10)  # remove

*. In Python, a list is mutable, ordered, and index-based-> 
 
 Mutable: You can change the list after creation.
 ex:nums[0] = 100

 Ordered: Order is preserved.
 ex: [1, 2, 3] ≠ [3, 2, 1]

 Index-based: Elements are accessed using index numbers.
 ex: nums[i]


#. How a List is Represented:
   -> list_name = [value1, value2, value3]
    Example: numbers = [10, 20, 30]
        names = ["Ram", "Shyam", "Aman"]
        mixed = [1, "hello", 3.5, True]
        empty = []

#. Why We Need Lists (Thought Process):
    ->If you need to store marks of 5 students:
        m1 = 85
        m2 = 90
        m3 = 78
        m4 = 88
        m5 = 92
    Issues:
       . Too many variables
       . Cannot use loops easily
       . Hard to sort, search, or update
       . Not scalable

        Solution With List:-> marks = [85, 90, 78, 88, 92]
     Now:
        . One variable
        . Easy looping
        . Easy operations (max, min, sort)
        . Scales to any size

II.>
#. How to Access the list elements in multiple ways:
   *. Accessing by Index (Most Basic):
        Concept: Each element in a list has a position number (index) starting from 0.
            Syntax:-> list_name[index]
                example: a = [10, 20, 30, 40]
                            print(a[0])  # 10
                            print(a[2])  # 30
    *. Negative Indexing (Access from End):
        Concept: Negative index accesses elements from the end.
            i.e, -1 → last element
                 -2 → second last
            Example:
                    print(a[-1])  # 40
                    print(a[-3])  # 20

        When to Use this Case: When list length is unknown but last element is needed.

    *. Accessing Using Slicing :
        Concept : Extract a sub-list (portion) from a list means taking a continuous part of a list
                  and creating a new list from it.
         Syntax:
                list[start : end : step]
                   . start → inclusive
                   . end → exclusive
                   . step → optional
        Example : a = [10, 20, 30, 40, 50]
                    print(a[1:4])     # [20, 30, 40]
                    print(a[:3])      # [10, 20, 30]
                    print(a[2:])      # [30, 40, 50]
                    print(a[::2])     # [10, 30, 50]
                    print(a[::-1])    # reverse list

        When to use it : “I need a range of elements, not just one.”

 *. Accessing Using Index + Loop:
    Concept: Access list elements using their index values while looping.
        Assume the list: a = [10, 25, 30, 45, 60]
            Example (using range() with index):
                -> for i in range(len(a)):
                    print("Index:", i, "Value:", a[i])

                Output:
                        Index: 0 Value: 10
                        Index: 1 Value: 25
                        Index: 2 Value: 30
                        Index: 3 Value: 45
                        Index: 4 Value: 60

                *.When to Use this Case: 
                    When index is required
                    When performing index-based comparison
                    When applying conditional logic using index
                    When modifying elements in-place based on position

III.> Basic List Operations (Python)

    #. Creating a List (Initialization):
     *. Concept: Creating a container to store multiple values in a single variable.
         Syntax:-> list_name = [value1, value2, value3]
         Example:
                a = [10, 20, 30]
                b = []
                c = list()
        When to use it:
                When you need to store multiple related values
                When number of elements is not fixed

    #. Accessing List Elements:
     *. Accessing by Index:
            Concept: Each element has an index starting from 0.
            Syntax:-> list_name[index]
            Example:
                    a = [10, 20, 30, 40]
                    print(a[0])   # 10
                    print(a[2])   # 30

     *. Negative Indexing:
            Concept: Access elements from the end of the list.
                    -1 → last element
                    -2 → second last
            Example:
                    print(a[-1])  # 40
                    print(a[-3])  # 20

     *. Accessing Using Slicing:
            Concept: Extract a portion (sub-list) from the list.
            Syntax:
                    list[start : end : step]
            Example:
                    a = [10, 20, 30, 40, 50]
                    print(a[1:4])   # [20, 30, 40]
                    print(a[:3])    # [10, 20, 30]
                    print(a[2:])    # [30, 40, 50]


    #. Updating (Modifying) List Elements:
     *. Concept: Lists are mutable, values can be changed.
        Example:
                a = [10, 20, 30]
                a[1] = 99
                print(a)   # [10, 99, 30]

    #. Adding Elements to a List:
     *. append():
            Concept: Adds one element at the end.
            Example:
                    a.append(40)

     *. insert():
            Concept: Adds an element at a specific index.
            Example:
                    a.insert(1, 15)

    #. Removing Elements from a List:
     *. remove(value):
            Concept: Removes the first occurrence of a value.
            Example:
                    a.remove(20)
     *. pop():
            Concept: Removes element using index (default last).
            Example:
                    a.pop()
                    a.pop(1)


    #. Traversing a List:  Traversing means going through each element one by one in a list (or any data structure) 
                            to see or use its values.
     *. Using for loop:
            Example:
                    for x in a:
                        print(x)
     *. Using while loop:
            Example:
                    i = 0
                    while i < len(a):
                        print(a[i])
                        i += 1

    #. Basic Built-in Operations:
     *. Length of list:
                len(a)
     *. Membership checking:
                20 in a
                50 not in a

    #. Simple List Copy:
     *. Correct way:
                b = a.copy()
        Concept: Creates a new list, avoids shared reference

IV.> Built-in Functions on Lists (Python)
    #. What are Built-in Functions?
     *. Concept:
            Built-in functions are predefined functions provided by Python
            that can be directly applied to lists.
            These functions do NOT belong to the list object itself.
        Key Difference:
            Built-in functions → function(list)
            List methods        → list.method()

    #. len() – Length of List:
     *. Concept:
            Returns the total number of elements present in the list.
        Syntax:-> 
                len(list_name)
        Example:
                a = [10, 20, 30, 40]
                print(len(a))   # 4
        When to use it:
                Looping through list
                Boundary checking
                Size validation

    #. max() – Maximum Element:
     *. Concept:
            Returns the largest element in the list.
        Syntax:-> 
                max(list_name)
        Example:
                a = [10, 45, 20, 30]
                print(max(a))   # 45
        Condition:
                All elements must be of comparable type

    #. min() – Minimum Element:
     *. Concept:
            Returns the smallest element in the list.
        Syntax:-> 
                min(list_name)
        Example:
                a = [10, 45, 20, 30]
                print(min(a))   # 10

    #. sum() – Sum of Elements:
     *. Concept:
            Returns the sum of all numeric elements in the list.
        Syntax:-> 
                sum(list_name)
        Example:
                a = [1, 2, 3, 4]
                print(sum(a))   # 10
        Condition: List must contain numeric values only

    #. sorted() – Sort List (Returns New List):
     *. Concept:
            Returns a new sorted list without modifying the original list.
        Syntax:-> 
                sorted(list_name)
                sorted(list_name, reverse=True)
        Example:
                a = [4, 1, 3, 2]
                b = sorted(a)

                print(b)   # [1, 2, 3, 4]
                print(a)   # [4, 1, 3, 2]

    #. any() – At Least One True:
     *. Concept:
            Returns True if at least one element in the list is True.
        Syntax:-> 
                any(list_name)
        Example:
                a = [0, False, 5]
                print(any(a))   # True

    #. all() – All Elements True:
     *. Concept:
            Returns True only if all elements in the list are True.
        Syntax:-> 
                all(list_name)
        Example:
                a = [1, True, 5]
                print(all(a))   # True

                b = [1, 0, 3]
                print(all(b))   # False

    #. abs() with List Elements: It removes the negative sign and gives the positive value(i.e, give only absolute values)
     *. Concept:
            abs() works on single values, not directly on a list.
            It must be applied element by element.
        Example:
                a = [-1, -2, 3]
                result = []
                for x in a:
                    result.append(abs(x))

                print(result)   # [1, 2, 3]

    #. Summary of Built-in Functions:
            len()     → number of elements
            max()     → largest element
            min()     → smallest element
            sum()     → sum of elements
            sorted()  → sorted copy of list
            any()     → at least one True
            all()     → all True

V.> Sorting and Reversing Lists (Python)
    #. Sorting a List:
     *. Concept: Sorting means arranging list elements in a specific order (ascending or descending).
         There are TWO ways to sort a list:
            1) Using sort()   → list method (modifies original list)
            2) Using sorted() → built-in function (creates new list)

     *. sort() – In-place Sorting:
        Concept:
                Sorts the list itself and changes the original list.
        Syntax:-> 
                list_name.sort()
                list_name.sort(reverse=True)
        Example:
                a = [40, 10, 30, 20]
                a.sort()
                print(a)   # [10, 20, 30, 40]

                a.sort(reverse=True)
                print(a)   # [40, 30, 20, 10]

        When to use it:
                When modifying the original list is allowed
                When extra memory should not be used

     *. sorted() – Returns a New Sorted List:
        Concept: Returns a sorted copy of the list without changing the original.
        Syntax:-> 
                sorted(list_name)
                sorted(list_name, reverse=True)
        Example:
                a = [40, 10, 30, 20]
                b = sorted(a)

                print(b)   # [10, 20, 30, 40]
                print(a)   # [40, 10, 30, 20]

        When to use it: When the original list must remain unchanged

    #. Reversing a List:
     *. Concept: Reversing means changing the order of elements so that the first element becomes last and the last becomes first.
                    NOTE: Reversing does NOT compare values.

     *. reverse() – In-place Reversal:
            Concept: Reverses the list and modifies the original list.
                Syntax:-> 
                        list_name.reverse()
                Example:
                        a = [10, 20, 30, 40]
                        a.reverse()
                        print(a)   # [40, 30, 20, 10]
                When to use it: When original list can be changed

     *. Reversing Using Slicing:
        Concept: Slicing with a negative step creates a new list  by traversing the original list from right to left.
                  This method does NOT modify the original list.
        Syntax:-> 
                list_name[start : end : step]
                list_name[::-1]

            Explanation of slicing [::-1]:
                    start → not specified → begins from end
                    end   → not specified → goes till start
                    step  → -1 → move backward one element at a time
        Example:
                a = [10, 20, 30, 40]
                b = a[::-1]

                print(b)   # [40, 30, 20, 10]
                print(a)   # [10, 20, 30, 40]

        When to use it:
                When original list must remain unchanged
                When a reversed copy is required

    #. Sorting vs Reversing (Important Difference):
        Sorting:
                Arranges elements based on value
                (small → large or large → small)
        Reversing:
                Only flips the order of elements
                No value comparison is performed

    #. Summary Table:
                sort()         → sorts original list
                sorted()       → returns new sorted list
                reverse()      → reverses original list
                slicing[::-1]  → returns reversed copy

VI.> List Slicing (Python)
    #. What is Slicing?
     *. Concept: Slicing means accessing a continuous portion (range) of elements from a list and creating a new list from it.
                 The original list is NOT modified.
        Key Idea:
                Indexing → single element
                Slicing  → multiple elements (sub-list)

    #. Slicing Syntax:
     *. General Syntax: list_name[start : end : step]
        Explanation:
                    start → starting index (inclusive)
                    end   → ending index (exclusive)
                    step  → gap between elements (optional)
        Note:
            If start is not given → starts from index 0
            If end is not given   → goes till last element
            Default step = 1

    #. Basic Slicing Examples:
        Example:
                a = [10, 20, 30, 40, 50]

                print(a[1:4])    # [20, 30, 40]
                print(a[:3])     # [10, 20, 30]
                print(a[2:])     # [30, 40, 50]
                print(a[:])      # [10, 20, 30, 40, 50] (full copy)

    #. Slicing with Step:
     *. Concept: Step decides how many indices to skip.
        Example:
                a = [10, 20, 30, 40, 50, 60]

                print(a[::2])    # [10, 30, 50]
                print(a[1::2])   # [20, 40, 60]

    #. Reverse List Using Slicing:
     *. Concept: Using a negative step traverses the list from right to left.
        Syntax:-> list_name[::-1]
        Example:
                a = [10, 20, 30, 40]
                b = a[::-1]

                print(b)   # [40, 30, 20, 10]
                print(a)   # [10, 20, 30, 40]

        Explanation:
                    start → end of list
                    end   → beginning of list
                    step  → -1 (move backward)

    #. Slicing with Negative Indices:
     *. Concept: Slicing also supports negative indices.
        Example:
                a = [10, 20, 30, 40, 50]

                print(a[-4:-1])   # [20, 30, 40]

    #. When to Use Slicing:
        Use slicing when:
                        You need a part of the list
                        You need a copy of the list
                        You want a reversed list
                        You want to skip elements systematically

VII.> List Varieties (Types of Lists in Python)
    #. What are List Varieties?
     *. Concept:
            List varieties refer to different forms in which lists
            can be created and used based on the type of data
            they store and their structure.

    #. Homogeneous List:
     *. Concept: A list that contains elements of the SAME data type.
        Example:
                numbers = [10, 20, 30, 40]
                names   = ["Ram", "Shyam", "Aman"]
        Use Case:
                Mathematical operations
                Marks, scores, ages

    #. Heterogeneous List:
     *. Concept: A list that contains elements of DIFFERENT data types.
        Example: data = ["Aryan", 20, 8.5, True]
        Use Case:
                Storing mixed information
                Records, profiles

    #. Nested List:
     *. Concept: A list that contains another list as its elements.
                 Used to represent multi-dimensional data.
        Example:
                matrix = [
                            [1, 2, 3],
                            [4, 5, 6]
                         ]
        Accessing Elements:
                    matrix[0]      # [1, 2, 3]
                    matrix[1][2]   # 6
        Use Case:
                Matrices
                Tables
                Graphs

    #. Empty List:
     *. Concept: A list with no elements.
        Example:
                a = []
                b = list()
        Use Case:
                Dynamic data storage
                Stack / Queue initialization

    #. List with Duplicate Elements:
     *. Concept: Lists allow duplicate values.
        Example:
                a = [10, 20, 20, 30]
        Use Case:
                Frequency counting
                Raw data storage

    #. List of Lists (2D / Multi-dimensional):
     *. Concept: Used to represent rows and columns.
        Example:
                table = [
                            ["ID", "Name", "Marks"],
                            [1, "Aman", 90],
                            [2, "Ravi", 85]
                        ]
        Use Case:
                Tabular data
                Database-like structures

    #. List Created Using list() Constructor:
     *. Concept:
            Creating list using iterable objects.
        Example:
                a = list("abc")      # ['a', 'b', 'c']
                b = list(range(5))   # [0, 1, 2, 3, 4]
        Use Case: Converting iterables into lists: 
                   . An iterable is something you can go through one element at a time
                    (like string, tuple, set, range).
                   .  Converting iterables into lists means turning those elements 
                    into a list so they can be indexed, modified, or reused.

    #. Summary of List Varieties:
                Homogeneous list     → same data type
                Heterogeneous list   → mixed data types
                Nested list          → list inside list
                Empty list           → no elements
                Duplicate list       → repeated elements
                2D / multi list      → table-like structure

VIII.> Stack and Queue Operations with Clear Concepts + Practical Examples
────────────────────────────────────────────────────────
A. STACK (LIFO – Last In, First Out)
────────────────────────────────────────────────────────
#. What is a Stack?
   *. Concept:
        A stack is a linear data structure where the
        last inserted element is removed first.

        Rule:
            LIFO → Last In, First Out

        In Python, a list works as a stack because:
            - append() adds at the end
            - pop() removes from the end


#. Stack Terminology + Meaning + List Mapping:
   *. push: Insert an element at the top of the stack
        List equivalent: append()

   *. pop: Remove the top-most element
        List equivalent: pop()

   *. peek / top: See the top element without removing it
        List equivalent: stack[-1]

   *. isEmpty:  Check whether stack is empty
        List equivalent: len(stack) == 0

#. Example 1: Basic Stack Operations
   Concept: Showing push, pop, peek, isEmpty together
   Code:
        stack = []
            # push
            stack.append(10)
            stack.append(20)
            stack.append(30)
            print(stack)        # [10, 20, 30]

            # peek
            print(stack[-1])    # 30

            # pop
            stack.pop()
            print(stack)        # [10, 20]

            # isEmpty
            print(len(stack) == 0)   # False

#. Example 2: Undo Feature (Text Editor)
   Concept: The last action must be undone first → Stack
   Code:
        actions = []
            actions.append("Type A")
            actions.append("Type B")
            actions.append("Delete C")

            undo_action = actions.pop()
            print("Undo:", undo_action)

#. Example 3: Reverse a String
   Concept: Stack reverses order naturally due to LIFO
   Code:
        s = "python"
        stack = []

        for ch in s:
            stack.append(ch)

        rev = ""
        while stack:
            rev += stack.pop()

        print(rev)   # nohtyp

#. Example 4: Function Call Idea (Call Stack)
   Concept: Functions return in reverse order of calls
   Code:
        calls = []
            calls.append("main()")
            calls.append("func1()")
            calls.append("func2()")
        while calls:
            print("Returning from:", calls.pop())

────────────────────────────────────────────────────────
B. QUEUE (FIFO – First In, First Out)
────────────────────────────────────────────────────────
#. What is a Queue?
   *. Concept:
        A queue is a linear data structure where the
        first inserted element is removed first.

        Rule: FIFO → First In, First Out

        Lists can simulate queues using:
            append()  → insert at rear
            pop(0)   → remove from front

#. Queue Terminology + Meaning + List Mapping:
   *. enqueue: Insert an element at the rear
        List equivalent: append()

   *. dequeue: Remove the element from the front
        List equivalent: pop(0)

   *. front: First element in queue
        List equivalent: queue[0]

   *. rear: Last element in queue
        List equivalent: queue[-1]

   *. isEmpty: Check if queue is empty
        List equivalent: len(queue) == 0

#. Example 1: Basic Queue Operations
   Concept: Showing enqueue, dequeue, front, rear
   Code:
        queue = []
        # enqueue
            queue.append(10)
            queue.append(20)
            queue.append(30)
            print(queue)       # [10, 20, 30]

        # front & rear
            print(queue[0])    # 10
            print(queue[-1])   # 30

        # dequeue
            queue.pop(0)
            print(queue)       # [20, 30]


#. Example 2: Ticket Counter System
   Concept: First person in line is served first
   Code:
        ticket_queue = []
            ticket_queue.append("Person A")
            ticket_queue.append("Person B")
            ticket_queue.append("Person C")

        served = ticket_queue.pop(0)
        print("Served:", served)

#. Example 3: Printer Queue
   Concept: Print jobs executed in arrival order
   Code:
        print_queue = []
            print_queue.append("doc1.pdf")
            print_queue.append("doc2.docx")
            print_queue.append("image.png")

        while print_queue:
            job = print_queue.pop(0)
            print("Printing:", job)

#. Example 4: Task Scheduling
   Concept: Tasks processed one by one in FIFO order
   Code:
        tasks = []
            tasks.append("Task 1")
            tasks.append("Task 2")
            tasks.append("Task 3")

        while tasks:
            current = tasks.pop(0)
            print("Processing:", current)

────────────────────────────────────────────────────────
C. Stack vs Queue (Quick Decision Guide)
────────────────────────────────────────────────────────
   Use STACK when:
            Latest element matters first
            Undo / Redo
            Reversal
            Backtracking

   Use QUEUE when:
            Order of arrival matters
            Scheduling
            Fair processing
            Waiting-line simulation



