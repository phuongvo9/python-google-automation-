import pytest

# Fixtures are used to separate parts of code that only run for tests. They are reusable pieces of test setups and teardown code that are shared across multiple tests. Fixtures benefit developers by assisting in keeping their tests clean and avoiding code duplication. Let’s look at an example of using a pytest in Python

class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)



# In this example, test_fruit_salad  requests fruit_bowl. When pytest recognizes this, it executes the fruit_bowl fixture function and takes the object it returns into test_fruit_salad as the fruit_bowl argument. 

