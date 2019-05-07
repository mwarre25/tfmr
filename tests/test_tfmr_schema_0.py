import unittest
import pandas as pd

class TestSchema0(unittest.TestCase):
    def test_blank_qryBushing(self):
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)
        pd.testing.assert_frame_equal(test_qryBushing, tfmr.schema_0.blank_qryBushing())


if __name__ == "__main__":
    unittest.main()
