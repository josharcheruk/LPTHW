formatter = "%r %r %r %r"

# No quotes for intergers
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
# No quotes for boolean operators
print formatter % (True, False, False, True)
# No quotes when calling variables
print formatter % (formatter, formatter, formatter, formatter)
# Alternative clearer formatting for the array
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So I said goodnight."
    )