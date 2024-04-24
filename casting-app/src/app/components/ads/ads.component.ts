import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Ad } from '../../interfaces/api';
import { AllservicesService } from '../../services/allservices.service';

@Component({
  selector: 'app-ads',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ads.component.html',
  styleUrl: './ads.component.css'
})
export class AdsComponent implements OnInit{
  ads: Ad[] = [];
  
  constructor(private myService: AllservicesService){}
  
  ngOnInit(): void {
    this.getAds()
  }

  getAds(){
    this.myService.getAds().subscribe((ads) => {
      this.ads = ads;
    });
  }

}
