import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

import { fields } from './schema.json';
import SignForm from './SignForm';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <SignForm {...{ fields }} />
  </React.StrictMode>,
  document.getElementById('root')
);
