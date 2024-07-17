calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    print(tuple([len(string), string.upper(), string.lower()]))
    count_calls()
def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    print(string in list_to_search)
    count_calls()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)