from kp_significator import get_full_significators

from kp_marriage import check_marriage
from kp_childbirth import check_childbirth
from kp_education import check_education
from kp_career import check_career
from kp_health import check_health
from kp_wealth import check_wealth
from kp_profession import check_profession
from kp_property import check_property
from kp_litigation import check_litigation


def run_prediction(dob, time, lat, lon):
    # STEP 1: Significators
    sig = get_full_significators(dob, time, lat, lon)

    # STEP 2: All predictions
    return {
        "marriage": check_marriage(sig),
        "childbirth": check_childbirth(sig),
        "education": check_education(sig),
        "career": check_career(sig),
        "health": check_health(sig),
        "wealth": check_wealth(sig),
        "profession": check_profession(sig),
        "property": check_property(sig),
        "litigation": check_litigation(sig)
    }


# TEST
if __name__ == "__main__":
    data = run_prediction("1982-12-04", "14:15", 28.6139, 77.2090)
    print(data)