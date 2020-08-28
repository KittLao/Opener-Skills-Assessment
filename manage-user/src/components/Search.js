import React from 'react';

export class Search extends React.Component {
    render() {
        const handleSubmit = this.props.handleSubmit;
        const handleChange = this.props.handleChange;
        return (
            <form  onSubmit={handleSubmit}>
                <input type="text" placeholder="Search for..." 
                onChange={handleChange}/>
                <input type="submit"/>
            </form>
        );
    }
}

export default Search;