#include "cruise.h"

bool CruiseControl::setSpeed(int speed) {
    return speed <= 120;
}