# Task3_file_handler.py
# Made for SaiKet Systems Internship

def file_handler():
    print("=== SaiKet Task 3: File Handler ===\n")
    
    filename = input("Enter file name ex: notes.txt : ")
    
    try:
        # FILE READ CHEYADAM
        with open(filename, 'r') as file:
            data = file.read()
            print(f"\nOriginal Content:\n{'-'*30}\n{data}\n{'-'*30}")
        
        # FIND & REPLACE
        find_word = input("\nWord to find: ")
        replace_word = input("Replace with: ")
        
        if find_word in data:
            modified_data = data.replace(find_word, replace_word)
            count = data.count(find_word)
            print(f"\n✅ Found '{find_word}' {count} times. Replaced with '{replace_word}'!")
        else:
            modified_data = data
            print(f"\n⚠️  Word '{find_word}' not found in file.")
        
        # FILE LO MALLI SAVE CHEYADAM
        with open(filename, 'w') as file:
            file.write(modified_data)
            print(f"✅ Changes saved to {filename}")
        
        # FINAL CONTENT CHUPINCHADAM
        print(f"\nModified Content:\n{'-'*30}\n{modified_data}\n{'-'*30}")
        
    # ERROR HANDLING
    except FileNotFoundError:
        print(f"\n❌ ERROR: File '{filename}' not found! Check name again.")
    except PermissionError:
        print(f"\n❌ ERROR: No permission to open '{filename}'")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
    
    print("\nMade for SaiKet Systems Internship")

if __name__ == "__main__":
    file_handler()
