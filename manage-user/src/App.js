import React from 'react';
import './App.css';

import Header from './components/Header';
import Search from './components/Search';
import UsersList from './components/UsersList';

class App extends React.Component {

  state = {
    query: "",
    queriedUsers: [],
    users: [
      {
        id: 0,
        name: "LBJ",
        email: "LBJ@gmail.com",
        phoneNumber: "23",
        department: "LBJdeparment",
        showAll: false
      },
      {
        id: 1,
        name: "KD",
        email: "KD@gmail.com",
        phoneNumber: "35",
        department: "KDdeparment",
        showAll: false
      },
      {
        id: 2,
        name: "SC",
        email: "SC@gmail.com",
        phoneNumber: "30",
        department: "SCdeparment",
        showAll: false
      },
      {
        id: 3,
        name: "JH",
        email: "JH@gmail.com",
        phoneNumber: "13",
        department: "JHdeparment",
        showAll: false
      },
      {
        id: 4,
        name: "RW",
        email: "RW@gmail.com",
        phoneNumber: "0",
        department: "RWdeparment",
        showAll: false
      }
    ]
  };

  constructor() {
    super();
    this.state.queriedUsers = this.state.users;
  }

  toggleDetailsOf = (idx) => {
    const newUsers = this.state.users;
    newUsers[idx].showAll = !newUsers[idx].showAll;

    this.setState({
      users: newUsers
    });
  }

  handleChange = (e) => {
    this.setState({
      query: e.target.value,
      users: this.state.users
    });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    const query = this.state.query;
    if(query.length === 0) {
      this.setState({
        ...this.state,
        queriedUsers: this.state.users
      });
    } else {
      const queriedUsers = this.state.users.filter(function (user) {
        return user.name === query || user.email === query;
      });
      this.setState({
        ...this.state,
        queriedUsers: queriedUsers
      });
    }
  }

  render() {
    return (
      <div className="App">
        <Header />
        <Search handleChange={this.handleChange} 
        handleSubmit={this.handleSubmit} />
        <UsersList users={this.state.queriedUsers} 
        toggleDetailsOf={this.toggleDetailsOf}/>
      </div>
    );
  }
}

export default App;
