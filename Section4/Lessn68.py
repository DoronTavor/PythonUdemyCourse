is_magician = False
is_expert = True

# Check if magician AND expert: "you are master magician"
message = "You are a master magician" if is_magician and is_expert else ""
if message: print(message)
# check if magician but not expert: "At least you're getting there"
message = "At least you're getting there" if is_magician and not is_expert else message
if message: print(message)
# if you arent magician : "You need magic powers"
message = "You need magic powers" if not is_magician else message
if message: print(message)