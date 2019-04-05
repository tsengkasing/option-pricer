import React, { useState } from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import { calcEuropeanOption } from '../util/api';

function EuropeanOption() {
    const [optionType, setOptionType] = useState('call');
    const [S, setS] = useState(100);
    const [sigma, setSigma] = useState(0.2);
    const [r, setR] = useState(0.01);
    const [q, setQ] = useState(0.5);
    const [T, setT] = useState(0.5);
    const [K, setK] = useState(100);
    const [result, setResult] = useState(null);

    const handleInput = {
        'optionType': e => setOptionType(e.target.value),
        'S': e => setS(e.target.value),
        'sigma': e => setSigma(e.target.value),
        'r': e => setR(e.target.value),
        'q': e => setQ(e.target.value),
        'T': e => setT(e.target.value),
        'K': e => setK(e.target.value),
    };

    function handleCalculate() {
        calcEuropeanOption(optionType, S, K, T, sigma, r, q).then(data => {
            setResult(data);
        }).catch(err => {
            alert(err);
        });
    }

    return (
        <section className="layout">
            <div className="input__field">
                <FormControl variant="outlined">
                    <InputLabel htmlFor="option-type">Option Type</InputLabel>
                    <Select
                        value={optionType}
                        onChange={handleInput['optionType']}
                        input={
                          <OutlinedInput
                            labelWidth={10}
                            name="option-type"
                            id="option-type"
                          />
                        }
                    >
                    <MenuItem value="call">Call Option</MenuItem>
                    <MenuItem value="put">Put Option</MenuItem>
                    </Select>
                </FormControl>
            </div>
            <div className="input__layout">
                <div className="input__field">
                    <TextField
                        label="Spot price"
                        value={S}
                        onChange={handleInput['S']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Volatility"
                        value={sigma}
                        onChange={handleInput['sigma']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Risk-free Interest Rate"
                        value={r}
                        onChange={handleInput['r']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Repo Rate"
                        value={q}
                        onChange={handleInput['q']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Time to Maturity"
                        value={T}
                        onChange={handleInput['T']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Strike"
                        value={K}
                        onChange={handleInput['K']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
            </div>
            <Button variant="contained" color="primary" onClick={handleCalculate}>Calculate</Button>
            {result !== null && <div className="calculated-result">
                <span>Result: {result}</span>
            </div>}
        </section>
    );
}

export default EuropeanOption;
