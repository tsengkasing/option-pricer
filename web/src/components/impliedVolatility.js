import React, { useState } from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import TextField from '@material-ui/core/TextField';
import Select from '@material-ui/core/Select';
import Button from '@material-ui/core/Button';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import CircularProgress from '@material-ui/core/CircularProgress';
import { calcImpliedVolatility } from '../util/api';

function ImpliedVolatility() {
    const [optionType, setOptionType] = useState('call');
    const [S, setS] = useState(100);
    const [r, setR] = useState(0.05);
    const [q, setQ] = useState(1.0);
    const [T, setT] = useState(3);
    const [K, setK] = useState(100);
    const [optionPremium, setOptionPremium] = useState(1);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleInput = {
        'optionType': e => setOptionType(e.target.value),
        'S': e => setS(e.target.value),
        'optionPremium': e => setOptionPremium(e.target.value),
        'r': e => setR(e.target.value),
        'q': e => setQ(e.target.value),
        'T': e => setT(e.target.value),
        'K': e => setK(e.target.value),
    };

    function handleCalculate() {
        setLoading(true);
        calcImpliedVolatility(optionType, S, K, T, r, q, optionPremium).then(data => {
            setResult(data);
            setLoading(false);
        }).catch(err => {
            alert(err);
            setLoading(false);
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
                        label="Spot price - S(0)"
                        value={S}
                        onChange={handleInput['S']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Risk-free Interest Rate - r"
                        value={r}
                        onChange={handleInput['r']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Repo Rate - q"
                        value={q}
                        onChange={handleInput['q']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Time to Maturity - T"
                        value={T}
                        onChange={handleInput['T']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Strike - K"
                        value={K}
                        onChange={handleInput['K']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
                <div className="input__field">
                    <TextField
                        label="Option Premium"
                        value={optionPremium}
                        onChange={handleInput['optionPremium']}
                        margin="normal"
                        variant="outlined"
                    />
                </div>
            </div>
            <Button variant="contained" color="primary" onClick={handleCalculate}>Calculate</Button>
            {loading && <div style={{margin: 16}}><CircularProgress /></div>}
            {result !== null && <div className="calculated-result">
                <span>Result: {result}</span>
            </div>}
        </section>
    );
}

export default ImpliedVolatility;
