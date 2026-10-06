import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("\nFace\tCount\tEmpirical P\tTheoretical P")

theoretical_probability = 1 / 6

for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    print(
        f"{face}\t{count}\t"
        f"{empirical_probability:.4f}\t\t"
        f"{theoretical_probability:.4f}"
    )

plt.figure(figsize=(8, 5))

plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xticks([1, 2, 3, 4, 5, 6])
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Fair Die Rolls - 1000 Simulations")

plt.savefig("die_rolls.png")
plt.show()

print("\nSaved die_rolls.png")