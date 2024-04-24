import { Component, OnInit } from '@angular/core';
import { Casting } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-filming',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './filming.component.html',
  styleUrl: './filming.component.css'
})
export class FilmingComponent implements OnInit{
  castings: Casting[] = [];
  filterName: string = 'Filming';

  constructor(private myService: AllservicesService) {}
  
  ngOnInit(): void {
    this.filterCastingsByName()
  }

  filterCastingsByName(): void {
    this.myService.getFilteredCastingsByName(this.filterName)
      .subscribe(
        (castings: Casting[]) => {
          this.castings = castings;
          // console.log('Filtered Castings:', this.castings);
        },
        (error) => {
          console.error('Error fetching castings:', error);
        }
      );
  }
}
