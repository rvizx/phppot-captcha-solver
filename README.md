# phppot CAPTCHA Solver 


### About

The "phppot CAPTCHA solver" aims to show that it's not a secure CAPTCHA implementation by solving the CAPTCHA's using OCR.
Security researchers can use this sample implementation to show that the instances that are using phppot's PHP CAPTCHA can be exploited which potentially leads to DoS and memory ro storage exahustion attacks based on the implementation.


### Usage

```bash
git clone https://github.com/rvizx/phppot-captcha-solver
cd phppot-captcha-solver
python3 -m pip install -r requirements.txt
python3 main.py
```

### Additional Notes

Before executing the `main.py`, you've to update the script and change the target details, also add the relavent "requests" related to the implementions of the target instance that's protected by the captcha to create a proper PoC.

phppot PHP CAPTCHA : https://phppot.com/php/php-captcha/
