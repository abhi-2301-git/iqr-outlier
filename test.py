from iqr_outlier.detection import detect_outliers
from iqr_outlier.removal import remove_outliers

def test_outlier_detection():
    data = [10, 12, 14, 15, 100, 18, 20, 22, 24, 30]
    assert detect_outliers(data) == [100]

def test_outlier_removal():
    data = [10, 12, 14, 15, 100, 18, 20, 22, 24, 30]
    assert remove_outliers(data).tolist() == [10, 12, 14, 15, 18, 20, 22, 24, 30]


if __name__ == "__main__":
    test_outlier_detection()
    test_outlier_removal()
    print("All tests passed!")
