def mysum(*items):
      if not items:
            return items
      output = items[0]
      for item in items[1:]:
            output += item
      if isinstance(output, int):
            return output
      if isinstance(output, str):
            return output
      else: return sum(output)

print(mysum((1,2,3,4,5)))
print(mysum([1,2,3,4,5]))
print(mysum(1,2,3,4,5))
print(mysum('hello','world'))