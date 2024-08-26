def calculate_love_score(name1, name2):
  
  true_count = 0
  love_count = 0
  found_count = 0

  combined_name = name1 + name2
  combined_name_upper = combined_name.upper()
  combined_name_nospace = combined_name_upper.replace(" ","")
  truelove = ["T","R","U","E","L","O","V","E"]
  truelove_count = []
  true_count =+ found_count
  
  for position, item in enumerate(truelove):
    found_count = combined_name_nospace.count(item)
    if position >= 0 and position <= 3:
       true_count += found_count
    elif position >= 4 and position <= 7:
       love_count += found_count
    if found_count == 1:
        print(f"{item} occurs {found_count} time")
    else:
        print(f"{item} occurs {found_count} times")

    if position ==3:
       print(f"Total = {true_count}")
    if position == 7:
       print(f"Total = {love_count}")

  print(f"Love Score = {true_count}{love_count}")

calculate_love_score(name1 = "David Pigman", name2 = "Christine Nguyen")