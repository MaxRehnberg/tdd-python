import pytest

from tdd.my_set import MySet


def test_new_set_is_empty():
    my_set = MySet()
    assert my_set.is_empty()


def test_set_with_element_is_not_empty():
    my_set = MySet(["a"])
    assert not my_set.is_empty()


def test_set_contains_element():
    my_set = MySet(["a"])
    assert "a" in my_set


def test_set_does_not_contain_element():
    my_set = MySet()
    assert "a" not in my_set


def test_equality_ignores_order():
    set_a = MySet(["a", "b"])
    set_b = MySet(["b", "a"])

    assert set_a == set_b


def test_add_ignorse_duplicates():
    my_set = MySet(["a"])
    my_set.add("a")
    assert len(my_set) == 1


def test_set_is_not_equal_to_other_types():
    assert MySet(["a"]) != "a"


@pytest.mark.parametrize("value", [None, ""], ids=["None", "empty string"])
def test_add_rejects_empty_values(value):
    my_set = MySet()
    with pytest.raises(ValueError):
        my_set.add(value)


@pytest.mark.parametrize("value", [None, ""], ids=["None", "empty string"])
def test_constructor_rejects_empty_values(value):
    with pytest.raises(ValueError):
        MySet([value])


def test_sets_are_equal_if_values_are_the_same():
    set_a = MySet(["a"])
    set_b = MySet(["a"])

    assert set_a == set_b


def test_sets_are_not_equal_if_values_are_different():
    set_a = MySet(["a"])
    set_b = MySet(["b"])

    assert set_a != set_b


def test_set_has_length():
    my_set = MySet(["a", "b"])
    assert len(my_set) == 2


def test_union_contains_elements_of_both_sets():
    expected = MySet(["a", "b", "c"])
    set_a = MySet(["a", "b"])
    set_b = MySet(["c"])

    actual = set_a | set_b

    assert actual == expected


def test_intersection_contains_only_shared_elements():
    expected = MySet(["a"])
    set_a = MySet(["a", "c"])
    set_b = MySet(["a", "b"])

    actual = set_a & set_b
    assert actual == expected


def test_is_subset_when_all_elements_are_in_other():
    set_a = MySet(["a"])
    set_b = MySet(["a", "b"])

    assert set_a.is_subset(set_b)


def test_is_not_subset_when_an_element_is_missing_from_other():
    set_a = MySet(["a", "b"])
    set_b = MySet(["a", "c"])

    assert not set_a.is_subset(set_b)


def test_set_is_subset_of_self():
    my_set = MySet(["a"])
    assert my_set.is_subset(my_set)


def test_is_superset_when_it_contains_all_elements_of_other():
    set_a = MySet(["a"])
    set_b = MySet(["a", "b"])

    assert set_b.is_superset(set_a)


def test_is_not_superset_when_other_has_an_element_it_lacks():
    set_a = MySet(["a", "b"])
    set_b = MySet(["a", "c"])

    assert not set_b.is_superset(set_a)


def test_set_is_superset_of_self():
    my_set = MySet(["a"])
    assert my_set.is_superset(my_set)


def test_is_proper_subset():
    set_a = MySet(["a"])
    set_b = MySet(["a", "b"])
    assert set_a < set_b
    assert set_b > set_a


def test_equal_sets_are_not_proper_subsets():
    set_a = MySet(["a", "b"])
    set_b = MySet(["a", "b"])
    assert not set_a < set_b


def test_is_proper_superset():
    set_a = MySet(["a"])
    set_b = MySet(["a", "b"])
    assert set_b > set_a
    assert set_a < set_b


def test_equal_sets_are_not_proper_supersets():
    set_a = MySet(["a", "b"])
    set_b = MySet(["a", "b"])
    assert not set_a > set_b


def test_delete_removes_element():
    expected = MySet(["a"])
    my_set = MySet(["a", "b"])
    my_set.delete("b")
    assert my_set == expected
