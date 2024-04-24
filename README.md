# phppot CAPTCHA Solver 


![Screenshot_20240424_140643](https://github.com/rvizx/phppot-captcha-solver/assets/84989569/7a2a0e15-3bac-461c-a4d5-76753e9c8ce4)


### About

The "phppot CAPTCHA solver" aims to show that it's not a secure CAPTCHA implementation by solving the CAPTCHA's using OCR.
Security researchers can use this sample implementation to show that the instances that are using phppot's PHP CAPTCHA can be exploited which potentially leads to DoS and memory or storage exahustion attacks based on the implementation.


### Usage

```bash
git clone https://github.com/rvizx/phppot-captcha-solver
cd phppot-captcha-solver
python3 -m pip install -r requirements.txt
python3 main.py
```

### Additional Notes

Before executing the `main.py`, update the script and change the target details, also add the relavent "requests" related to the implementions of the target instance that's protected by the captcha to create a proper PoC.

phppot PHP CAPTCHA : https://phppot.com/php/php-captcha/
