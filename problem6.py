def first_tool_position(tools, wanted):
    for i in range(len(tools)):
        if tools[i]==wanted:
            return i       
    return -1
def all_tool_positions(tools, wanted):
    positions=[]
    for i in range(len(tools)):
        if tools[i]==wanted:
            positions.append(i)
    return positions
tools = ["hammer", "drill", "saw", "drill", "wrench"]
drill_first=first_tool_position(tools, "drill")
drill_all=all_tool_positions(tools, "drill")
print(f"first position = {drill_first}, all positions = {drill_all}")
tape_first=first_tool_position(tools, "tape")
tape_all=all_tool_positions(tools, "tape")
print(f"first position = {tape_first}, all positions = {tape_all}")
