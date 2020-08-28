import React from 'react';
import './App.css';

import Header from './components/Header';
import UsersList from './components/UsersList';

class App extends React.Component {

  state = {
    query: "",
    users: [
      {
        id: 0,
        name: "X",
        email: "X@gmail.com",
        phoneNumber: "123",
        department: "dep",
        showAll: false
      },
      {
        id: 1,
        name: "Y",
        email: "Y@gmail.com",
        phoneNumber: "124",
        department: "dep",
        showAll: false
      },
      {
        id: 2,
        name: "A",
        email: "A@gmail.com",
        phoneNumber: "125",
        department: "dep",
        showAll: false
      },
      {
        id: 3,
        name: "B",
        email: "B@gmail.com",
        phoneNumber: "126",
        department: "dep",
        showAll: false
      },
      {
        id: 4,
        name: "C",
        email: "C@gmail.com",
        phoneNumber: "127",
        department: "dep",
        showAll: false
      }
    ]
  };

  toggleDetailsOf = (idx) => {
    const newUsers = this.state.users;
    newUsers[idx].showAll = !newUsers[idx].showAll;

    this.setState({
      users: newUsers
    });
  }

  searchFor = (query) => {

  }

  render() {
    return (
      <div className="App">
        <Header />
        <section className="section">
          <form onSubmit={this.searchFor}>
            <input placeholder="Search for..." 
            type="text"
            value="" />
          </form>
        </section>
        <UsersList users={this.state.users} 
        toggleDetailsOf={this.toggleDetailsOf}/>
      </div>
    );
  }
}

export default App;
