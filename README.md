# PythonDisjointSet
Quick Disjoint Set implementation for Python3
## Installation
-Fastest would be to copy-paste the contents of DisjointSet.py into your code

-Or you could download DisjointSet.py and throw it in your project directory. Use "from DisjointSet import *" to use it in your code

-You could clone https://github.com/asawitt/PythonDisjointSet/ , move DisjointSet.py to your project directory, then use the above import statement if you really want to. Don't. 

## Usage
### Create a new DisjointSet
sets = DisjointSet()
### Add a new Set
sets.addSet(index)
### Add a value to an existing set
sets.addToSet(setIndex,value)
### Union
-combines merges set with index2 into set with index1
sets.union(index1, index2)
### Finding a value
-Returns the index of the set which contains the given value in O(n) time.
-If the value is in more than one set it will return the index of the first containing set found. 
sets.find(value)
### Printing
sets.printSets()
### Removing a set
sets.removeSet(index)
### Getting the size of a set
-Returns the size of the set with the given setIndex in O(1) time
sets.getSize(setIndex)



## License
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
