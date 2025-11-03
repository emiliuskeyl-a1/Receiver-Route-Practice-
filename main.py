from playgen import generate_playcall, route_library
import matplotlib.pyplot as plt

if __name__ == "__main__":
    playcall_str = generate_playcall()
    print(playcall_str)
    playcall = playcall_str.split()

plt.figure(figsize=(6, 10))
for route_name in playcall:
    if route_name in route_library:
        points = route_library[route_name]
        x, y = zip(*points)
        plt.plot(x, y, marker='o', label=route_name)

plt.title("Receiver Routes")
plt.xlabel("Yards nach vorne")
plt.ylabel("Seitwärtsposition")
plt.legend()
plt.grid(True)
plt.show()