import math


def dot_product(vector_a: list[float], vector_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vector_a, vector_b))


def magnitude(vector: list[float]) -> float:
    return math.sqrt(sum(value * value for value in vector))


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    dot = dot_product(vector_a, vector_b)

    magnitude_a = magnitude(vector_a)
    magnitude_b = magnitude(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")

    return dot / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    python_vector = [1, 2, 3]
    programming_vector = [1,2,3]
    cricket_vector = [-1, 0, 1]
    vector_a = [1,2,3]
    vector_b = [2,4,6]

    print(
        "Python vs Programming:",
        cosine_similarity(python_vector, programming_vector),
    )
    print(
        "Same direction, different size:",
        cosine_similarity(vector_a, vector_b),
    )
    print(
        "Python vs Cricket:",
        cosine_similarity(python_vector, cricket_vector),
    )