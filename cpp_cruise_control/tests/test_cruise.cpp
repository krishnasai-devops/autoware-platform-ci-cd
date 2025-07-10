#include "gtest/gtest.h"
#include "../include/cruise.h"

TEST(CruiseControlTest, SpeedWithinLimit) {
    CruiseControl cc;
    EXPECT_TRUE(cc.setSpeed(80));
}