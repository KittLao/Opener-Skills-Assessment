  
import React, { Component } from 'react';
import User from './User';

class UsersList extends Component {
    render() {
        return this.props.users.map((user) => (
            <User user={user} toggleDetailsOf={this.props.toggleDetailsOf} />
        ));
    }
}

export default UsersList;